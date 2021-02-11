resource "aws_security_group" "busybox" {
  name        = var.security
  description = "Regras para liberar portas"

ingress {
    description = "Endereco para liberar"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.cidr]
  }



  tags = {
    "Name" = "sg_develop"
    "Provider" = "terraform"
  }
  
}