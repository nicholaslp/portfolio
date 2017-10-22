import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
  {
    'title': "Work Example 1",
    "href":"https://www.example.com",
    "desc":"Lorem ipsum",
    'image': {
      'desc': "Work Example 1",
      'src': "images/example1.png",
      'comment': "Work Example 1"
    }
  },
  {
    'title': "Work Example 2",
    "href":"https://www.example.com",
    "desc":"Lorem ipsum",
    'image': {
      'desc': "Serverless",
      'src': "images/example2.png",
      'comment': "A Serverless Portfolio"
    }
  },
  {
    'title': "Work Example",
    "href":"https://www.example.com",
    "desc":"Lorem ipsum",
    'image': {
      'desc': "Work Example 3",
      'src': "images/example3.png",
      'comment': `“Bengal cat” by roberto shabs is licensed under CC BY 2.0
             https://www.flickr.com/photos/37287295@N00/2540855181`
    }
  }
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
