data = File.read("day4.txt").split("\n\n")
numbers = data[0].split(",").map(&:to_i)
boards = data[1..].map{_1.split("\n").map{|l|l.split.map(&:to_i)}}
scores = Array.new

numbers.each do | num |
    boards.dup.each do | board |
        (0...boards[0].length).each do | row |
            (0...boards[0].length).each do | col |
                board[row][col] = -1 if board[row][col] == num
            end
        end
        columns = board.transpose
        (0...boards[0].length).each do | i |
            if board[i].all?(&:negative?) || columns[i].all?(&:negative?)
                scores << board.flatten.select(&:positive?).sum * num
                boards.delete(board)
            end
        end
    end
end

puts "Part one:", scores[0]
puts "Part two:", scores[-1]