import "./HabitComponent.css";

type Habit = {
  Habit: string;
  Checked: boolean;
};

export const HabitComponent = () => {
  const habits: Array<Habit> = [
    {
      Habit: "Test some extremely long habit which wsohuldsg overfill the line",
      Checked: false,
    },
    { Habit: "Dog", Checked: false },
    { Habit: "Cat", Checked: false },
  ];

  return (
    <div className="habits_wrapper">
      <h2 className="habits_title">My Habits</h2>
      <ul className="habits_ul">
        {habits.map((habit) => (
          <li key={habit.Habit} className="habit_li">
            <span className="habit_title">{habit.Habit}</span>
            <input
              type="checkbox"
              // checked={habit.Checked}
              className="habit_checked"
            />
          </li>
        ))}
      </ul>
    </div>
  );
};
