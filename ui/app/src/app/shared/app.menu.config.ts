import { MenuRootItem } from 'ontimize-web-ngx';

import { AdministratorCardComponent } from './Administrator-card/Administrator-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { DogSizePriceHistoryCardComponent } from './DogSizePriceHistory-card/DogSizePriceHistory-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { NotificationCardComponent } from './Notification-card/Notification-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SystemLogCardComponent } from './SystemLog-card/SystemLog-card.component';

import { WalkRequestCardComponent } from './WalkRequest-card/WalkRequest-card.component';

import { WalkRequestDogCardComponent } from './WalkRequestDog-card/WalkRequestDog-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerAvailabilityCardComponent } from './WalkerAvailability-card/WalkerAvailability-card.component';

import { WalkerHistoryCardComponent } from './WalkerHistory-card/WalkerHistory-card.component';

import { WalkerPriceCardComponent } from './WalkerPrice-card/WalkerPrice-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Administrator', name: 'ADMINISTRATOR', icon: 'view_list', route: '/main/Administrator' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'DogSizePriceHistory', name: 'DOGSIZEPRICEHISTORY', icon: 'view_list', route: '/main/DogSizePriceHistory' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Notification', name: 'NOTIFICATION', icon: 'view_list', route: '/main/Notification' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'SystemLog', name: 'SYSTEMLOG', icon: 'view_list', route: '/main/SystemLog' }
    
        ,{ id: 'WalkRequest', name: 'WALKREQUEST', icon: 'view_list', route: '/main/WalkRequest' }
    
        ,{ id: 'WalkRequestDog', name: 'WALKREQUESTDOG', icon: 'view_list', route: '/main/WalkRequestDog' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerAvailability', name: 'WALKERAVAILABILITY', icon: 'view_list', route: '/main/WalkerAvailability' }
    
        ,{ id: 'WalkerHistory', name: 'WALKERHISTORY', icon: 'view_list', route: '/main/WalkerHistory' }
    
        ,{ id: 'WalkerPrice', name: 'WALKERPRICE', icon: 'view_list', route: '/main/WalkerPrice' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AdministratorCardComponent

    ,DogCardComponent

    ,DogSizePriceHistoryCardComponent

    ,FeedbackCardComponent

    ,NotificationCardComponent

    ,OwnerCardComponent

    ,PaymentCardComponent

    ,ReviewCardComponent

    ,SystemLogCardComponent

    ,WalkRequestCardComponent

    ,WalkRequestDogCardComponent

    ,WalkerCardComponent

    ,WalkerAvailabilityCardComponent

    ,WalkerHistoryCardComponent

    ,WalkerPriceCardComponent

];