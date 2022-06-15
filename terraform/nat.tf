resource "aws_eip" "nat" {

	depends_on = [
	  aws_internet_gateway.igw
	  ]
}


resource "aws_nat_gateway" "nat" {
	allocation_id = aws_eip.nat.id
	subnet_id     = aws_subnet.public-us-east-1a.id


	tags = {
	  Name = "nat"
	}

	depends_on = [aws_internet_gateway.igw]
}