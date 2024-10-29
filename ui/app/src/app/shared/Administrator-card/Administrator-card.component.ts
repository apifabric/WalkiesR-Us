import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Administrator-card.component.html',
  styleUrls: ['./Administrator-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Administrator-card]': 'true'
  }
})

export class AdministratorCardComponent {


}