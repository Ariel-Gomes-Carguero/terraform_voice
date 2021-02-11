output "ip" {
  value = aws_instance.leroy.public_ip
}

output "nome" {
    value = aws_instance.leroy.tags.Name
  
}