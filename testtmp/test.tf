provider "google" {
  project     = "sap-se-cx-sre-sdev"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = "${file("/Users/D073341/work/sap-se-cx-sre-sdev-5a5f8649b0a9.json")}"
}

resource "google_compute_instance" "available" {
  project      = "sap-se-cx-sre-sdev"
  zone         = "us-central1-a"
  name         = "test-vm123"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "centos-6-v20181113"
    }
  }

  network_interface {
    network       = "default"
    access_config = {}
  }
}
