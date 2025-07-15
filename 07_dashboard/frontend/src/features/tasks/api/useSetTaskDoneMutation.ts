import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { TasksResponse } from "../types"

type payload = {task_id: string, completed: boolean};

export const useSetTaskDoneMutation = () => 
  useMutation<TasksResponse, Error, payload>({
    mutationFn: ({task_id, completed}) => 
      api.post<TasksResponse>(`/todo/toggle`, {"task_id": task_id, "completed": completed})
    .then((res) => res.data),
});