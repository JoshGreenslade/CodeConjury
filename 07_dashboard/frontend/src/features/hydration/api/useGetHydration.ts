import { useQuery } from "@tanstack/react-query";
import api from "../../../common/axios";

type HydrationData = {
  hydration: number;
}

export const useGetHydration = () => useQuery<HydrationData>({
  queryKey: ["hydration", "today"],
  queryFn: () => api.get<HydrationData>("/hydration/today").then(res => res.data),
  staleTime: Infinity,
});
