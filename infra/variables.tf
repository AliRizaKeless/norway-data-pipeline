variable "resource_group_name" {
  description = "Azure Resource Group name"
  type        = string
  default     = "rg-norway-data-pipeline"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "westeurope"
}

variable "storage_account_name" {
  description = "Azure Storage Account name"
  type        = string
  default     = "norwaydatapipeline01"
}

variable "container_name" {
  description = "Blob container name"
  type        = string
  default     = "data"
}
