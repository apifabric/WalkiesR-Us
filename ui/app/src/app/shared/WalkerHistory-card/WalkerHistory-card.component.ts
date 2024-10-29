import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkerHistory-card.component.html',
  styleUrls: ['./WalkerHistory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkerHistory-card]': 'true'
  }
})

export class WalkerHistoryCardComponent {


}