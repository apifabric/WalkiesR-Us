import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WalkRequest-card.component.html',
  styleUrls: ['./WalkRequest-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WalkRequest-card]': 'true'
  }
})

export class WalkRequestCardComponent {


}