provider "google" {
  project = "sap-se-cx-sre-sqa"
  region = "europe-west1"
  zone = "europe-west1-b"
  credentials = "${file("/Users/D073341/work/tereaform/sap-se-cx-sre-sqa-f54805741b08.json")}"
}
