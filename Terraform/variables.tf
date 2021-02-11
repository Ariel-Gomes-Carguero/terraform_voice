variable "ami" {
    default = "ami-04d29b6f966df1537"
  
}

variable "instance_type" {
    default = "t2.micro"
  
}

variable "cidr" {
    default = "0.0.0.0/0"
    
  
}

variable "security" {
    default = "sg_develop"
  
}

variable "ec2name" {
    default = "Terraform"
  
}