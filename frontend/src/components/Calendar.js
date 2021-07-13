import React from 'react'
import Calendar from 'react-awesome-calendar';

const events = [{
    id: 1,
    color: '#fd3153',
    from: '2021-07-10T18:00:00+00:00',
    to: '2021-07-11T19:00:00+00:00',
    title: 'This is an event'
}, {
    id: 2,
    color: '#1ccb9e',
    from: '2019-05-01T13:00:00+00:00',
    to: '2019-05-05T14:00:00+00:00',
    title: 'This is another event'
}, {
    id: 3,
    color: '#3694DF',
    from: '2019-05-05T13:00:00+00:00',
    to: '2019-05-05T20:00:00+00:00',
    title: 'This is also another event'
}];


function Cal() {
    return (
        <div className="container">
                <Calendar
                    events={events}
                />
            
        </div>
    )
}


export default Cal;