import axios from 'axios';

const LOAD_REPOS_SUCCESS = 'LOAD_REPOS_SUCCESS';
const LOAD_REPOS = 'LOAD_REPOS';

const initialState = {
    isLoading: false,
    list: []
};

export const loadRepos = () => (dispatch) => {
    dispatch({
        type: LOAD_REPOS,
    });

    // https://api.github.com/users/iu5team/repos
    
    //axios.get('http://www.splashbase.co/api/v1/images/latest?images_only=true')
    //axios.get('https://api.unsplash.com/photos/?client_id=cce30bf06aa95f3011a2083b8f20112ae961e2a16d2a3e5b01d96392b3eaed39')
    axios({
        method: 'get',
        url: 'https://api.unsplash.com/photos/?client_id=cce30bf06aa95f3011a2083b8f20112ae961e2a16d2a3e5b01d96392b3eaed39',
        responseType: 'stream'
    })    
        .then(response => {
            setTimeout(() => {                
                dispatch({             
                    type: LOAD_REPOS_SUCCESS,
                    payload: response.data
                })
            }, 1300)
        }).catch(() => {
            // Если ошибка, то будет пустой
            dispatch({
                type: LOAD_REPOS_SUCCESS,
                payload: []
            })
        });
};

function reducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_REPOS:
            return Object.assign({}, state, {
                isLoading: true
            });
        case LOAD_REPOS_SUCCESS:
            return Object.assign({}, state, {
                list: action.payload,
                isLoading: false
            });
        default: return state;
    }
}

export default reducer;
