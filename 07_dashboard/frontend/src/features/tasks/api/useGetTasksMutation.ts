import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { TasksResponse } from "../types"


export const useGetTasksMutation = () => 
  useMutation<TasksResponse, Error, string>({
    mutationFn: (prompt) => 
      api.post<TasksResponse>("/todo/", {"context": prompt})
    .then((res) => res.data),
});