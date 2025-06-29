import { useQuery } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { HabitGet } from "../types";

export const useGetHabits = () => useQuery<Array<HabitGet>>({
  queryKey: ["habits"],
  queryFn: () => api.get<Array<HabitGet>>("/habits").then(res => res.data),
  staleTime: Infinity,
});