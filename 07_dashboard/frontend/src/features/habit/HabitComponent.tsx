import { useEffect, useState } from "react";
import "./HabitComponent.css";
import { useGetHabits } from "./api/useGetHabits";
import type { Habit } from "./types";
import { usePostHabit } from "./api/usePostHabit";

export const HabitComponent = () => {
  const { data, isLoading, error } = useGetHabits();
  const [habits, setHabits] = useState<Array<Habit>>([]);
  const { mutate: mutateHabit } = usePostHabit();

  useEffect(() => {
    if (data !== undefined) {
      setHabits(data);
    }
  }, [data]);

  const handleCheckboxChange = (habit: string, checked: boolean) => {
    setHabits((prev) =>
      prev.map((h) => (h.Habit === habit ? { ...h, Checked: checked } : h))
    );

    mutateHabit({ Habit: habit, Checked: checked });
  };

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading data.</p>;

  return (
    <div className="habits_wrapper">
      <h2 className="habits_title">My Habits</h2>
      <ul className="habits_ul">
        {habits.map((habit) => (
          <li key={habit.Habit} className="habit_li">
            <span className="habit_title">{habit.Habit}</span>
            <input
              type="checkbox"
              checked={habit.Checked}
              className="habit_checked"
              onChange={(e) =>
                handleCheckboxChange(habit.Habit, e.target.checked)
              }
            />
          </li>
        ))}
      </ul>
    </div>
  );
};
