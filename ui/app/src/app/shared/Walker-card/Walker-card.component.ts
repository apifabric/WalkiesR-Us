import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Walker-card.component.html',
  styleUrls: ['./Walker-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Walker-card]': 'true'
  }
})

export class WalkerCardComponent {


}