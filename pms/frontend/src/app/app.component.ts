import { Component } from '@angular/core';

import { Task } from './config.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  task: Task | undefined;

  title = 'frontend';

  showTask() {
    this.configService.
  }
}
