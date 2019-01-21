import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
//import ui from './ui';
import repos from './repos';

// const store = createStore(combineReducers({
//     ui,
//     repos
// }), applyMiddleware(thunk));

const store = createStore(combineReducers({repos}), applyMiddleware(thunk));

export default store;
