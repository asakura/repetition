-module(solution).
-export([main/0]).

                                                % Complete the solve function below.
solve(MealCost, TipPercent, TaxPercent) ->
    Tip = MealCost * (TipPercent / 100),
    Tax = MealCost * (TaxPercent / 100),
    TotalCost = MealCost + Tip + Tax,

    io:fwrite("~B~n", [round(TotalCost)]).

main() ->
    {MealCost, _} = string:to_float(string:chomp(io:get_line(""))),
    {TipPercent, _} = string:to_integer(string:chomp(io:get_line(""))),
    {TaxPercent, _} = string:to_integer(string:chomp(io:get_line(""))),

    solve(MealCost, TipPercent, TaxPercent),

    ok.
