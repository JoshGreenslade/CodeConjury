export type TasksResponse = {
  results: TasksData
}

export type TasksData = {
  recommended: Array<Task>;
  summary: string;
}

export type Task = {
  task_id: string;
  title: string;
  reason: string;
  effort: number;
}
