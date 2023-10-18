from island import Island

let islands = [10]
let model = new ModelNavigator(islands, 500)


class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.islands = islands
        self.crew = crew

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        # crew = int(input("How many crewmates are sent to each island?"))
        profit_crew_list =  []
        for island in self.islands:
            crew_needed = self.crew - island.marines
            profit = ((crew_needed/island.marines)*island.money)
            profit_crew_list.append((profit, crew_needed))

        available_crew = self.crew    
        n = len(profit_crew_list)
        dp = [0] * (available_crew + 1)

        for i in range(n):
            for crew in range(available_crew, 0, -1):
                profit, required_crew = profit_crew_list[i]
                if required_crew <= crew:
                    dp[crew] = max(dp[crew], dp[crew - required_crew] + profit)

        chosen_crew = available_crew
        results = []

        for i in range(n - 1, -1, -1):
            profit, required_crew = profit_crew_list[i]
            if required_crew <= chosen_crew and dp[chosen_crew] == dp[chosen_crew - required_crew] + profit:
                results.append((profit, required_crew))
                chosen_crew -= required_crew

        return results

        
            # profit.append(min((self.crew*island.money)/island.marines, island.money))
        


        # island_crew_list = [(island, crew) for island in self.islands]
        # return island_crew_list

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError
