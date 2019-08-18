% Enter your code here. Read input from STDIN. Print output to STDOUT
% Your class should be named solution

-module(solution).
-export([main/0]).

main() ->
    InputString = io:get_line(""),
    io:fwrite("Hello, World.~n"),
    io:fwrite(InputString).
