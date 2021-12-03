file = File.open("day3.txt")
data = file.readlines.map(&:chomp)

gamma = ""
epsilon = ""

(0..data.length - 1).each do | i |
    data[i] = data[i].split("").map(&:to_i)
end

columns = data.transpose()

columns.each do | i |
    if i.sum > i.length / 2
        gamma += "1"
        epsilon += "0"
    else
        gamma += "0"
        epsilon += "1"
    end
end

puts "Part one: #{gamma.to_i(2) * epsilon.to_i(2)}"

co_data =* data

(0..co_data[0].length - 1).each do | i |
    temp = Array.new
    columns = co_data.transpose()
    if columns[i].sum == columns[i].length / 2
        a = 1
    elsif columns[i].sum > columns[i].length / 2
        a = 1
    else
        a = 0
    end
    co_data.each do | j |
        if j[i] == a
            temp << j
        end
    end
    co_data =* temp
    if co_data.length == 1
        $c = co_data[0].join("")
    end
end

ox_data =* data

(0..ox_data[0].length - 1).each do | i |
    temp = Array.new
    columns = ox_data.transpose()
    if columns[i].sum == columns[i].length / 2
        a = 0
    elsif columns[i].sum > columns[i].length / 2
        a = 0
    else
        a = 1
    end
    ox_data.each do | j |
        if j[i] == a
            temp << j
        end
    end
    ox_data =* temp
    if ox_data.length == 1
        $d = ox_data[0].join("")
    end
end

puts "Part two: #{$c.to_i(2) * $d.to_i(2)}"