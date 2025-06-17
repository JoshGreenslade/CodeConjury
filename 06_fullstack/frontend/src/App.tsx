import React, { useState, useRef, useEffect } from "react";

const PullDownCounter: React.FC = () => {
  const [value, setValue] = useState(0);
  const [counter, setCounter] = useState(0);
  const frameRef = useRef<number | null>(null);
  const lastTick = useRef<number>(performance.now());

  useEffect(() => {
    const tick = (now: number) => {
      const elapsed = now - lastTick.current;

      if (value >= 30) {
        const rate = Math.max(100 - value, 10); // ms per tick
        if (elapsed >= rate) {
          setCounter((prev) => prev + 1);
          lastTick.current = now;
        }
      } else {
        lastTick.current = now;
      }

      frameRef.current = requestAnimationFrame(tick);
    };

    frameRef.current = requestAnimationFrame(tick);

    return () => {
      if (frameRef.current) {
        cancelAnimationFrame(frameRef.current);
      }
    };
  }, [value]);

  const handleRelease = () => {
    setValue(0);
  };

  return (
    <div style={styles.wrapper}>
      <div style={styles.sliderWrapper}>
        <input
          type="range"
          min={0}
          max={100}
          value={value}
          onInput={(e) => setValue(Number(e.currentTarget.value))}
          onMouseUp={handleRelease}
          onTouchEnd={handleRelease}
          style={styles.verticalSlider}
        />
      </div>
      <div style={styles.counter}>{counter}</div>
    </div>
  );
};

export default PullDownCounter;

const styles: Record<string, React.CSSProperties> = {
  wrapper: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    height: "300px",
    justifyContent: "center",
  },
  sliderWrapper: {
    height: "60px",
    width: "200px",
    transform: "rotate(90deg)",
    marginBottom: "80px",
  },
  verticalSlider: {
    width: "100%",
    height: "100%",
    appearance: "none",
    WebkitAppearance: "none",
    background: "#ddd",
    borderRadius: "8px",
    cursor: "grab",
  },
  counter: {
    fontSize: "2rem",
    fontWeight: "bold",
  },
};
