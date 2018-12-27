provider "google" {
  project     = "sap-se-cx-sre-sdev"
  region      = "europe-west1"
  zone        = "europe-west1-b"
  credentials = "${file("/Users/D073341/work/sap-se-cx-sre-sdev-bd164287eb29.json")}"
}
