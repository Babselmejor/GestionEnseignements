import { Component, OnInit } from "@angular/core";

@Component({
  selector: "app-index-navbar",
  templateUrl: "./index-navbar.component.html",
  styleUrl: "./index-navbar.component.css",
})
export class IndexNavbarComponent implements OnInit {
  navbarOpen = false;

  constructor() {}

  ngOnInit(): void {}

  setNavbarOpen() {
    this.navbarOpen = !this.navbarOpen;
  }
}
