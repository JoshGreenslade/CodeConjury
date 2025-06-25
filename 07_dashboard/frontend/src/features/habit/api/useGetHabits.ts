import { useQuery } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { Habit } from "../types";

export const useGetHabits = () => useQuery<Array<Habit>>({
  queryKey: ["habits"],
  queryFn: () => api.get<Array<Habit>>("/habits").then(res => res.data),
  staleTime: Infinity,
});