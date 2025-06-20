import { useState, useEffect, useRef } from "react";
import { useGetHydration } from "./api/useGetHydration";
import { usePostHydration } from "./api/usePostHydration";
import "./HydrationComponent.css";

export const HydrationComponent = () => {
  const [hydration, setHydration] = useState(0.0);
  const [sliderValue, setSliderValue] = useState(0);
  const intervalRef = useRef<NodeJS.Timeout | null>(null);
  const debounceRef = useRef<NodeJS.Timeout | null>(null);
  const { data, isLoading, error } = useGetHydration();
  const mutation = usePostHydration();

  useEffect(() => {
    if (data?.hydration !== undefined) {
      setHydration(data.hydration);
    }
  }, [data]);

  // Adjust loop rate when sliderValue changes
  useEffect(() => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }

    if (sliderValue >= 10) {
      intervalRef.current = setInterval(() => {
        setHydration((prev) => prev + (sliderValue - 10) / 80);
      }, 1);
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
        intervalRef.current = null;
      }
    };
  }, [sliderValue]);

  const handleInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    setSliderValue(Number(e.target.value));
  };

  const handleRelease = () => {
    setSliderValue(0); // triggers stop in tick loop

    if (debounceRef.current) {
      clearTimeout(debounceRef.current);
    }
    const val = Math.floor(hydration);
    debounceRef.current = setTimeout(() => {
      mutation.mutate({ hydration: val });
    }, 500);
  };

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading data.</p>;

  return (
    <div className="wrapper">
      <div className="sliderWrapper">
        <input
          type="range"
          min={0}
          max={100}
          value={sliderValue}
          onInput={handleInput}
          onMouseUp={handleRelease}
          onTouchEnd={handleRelease}
          className="verticalSlider"
        />
        <p className="counter">{Math.floor(hydration)}</p>
      </div>
    </div>
  );
};
