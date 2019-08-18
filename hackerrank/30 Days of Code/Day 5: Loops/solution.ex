defmodule Solution do
  n = IO.read(:stdio, :line)

  n = n
  |> String.trim()
  |> String.to_integer()

  Enum.each(1..10, fn i ->
    IO.puts "#{n} x #{i} = #{n * i}"
  end)
end
