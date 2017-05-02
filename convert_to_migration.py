num_queries = 0
out = open("output.php", "w+")

with open("input.sql") as f:
    for line in f:
        if line != '\n' and not line.startswith('--'):
            new_line = "$this->query('" + line.replace("'", "\\'").replace("\n", "") + "');\n"
            out.write(new_line)
            num_queries += 1
print "Converted " + str(num_queries) + " queries"
