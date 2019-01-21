import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

import './ListItem.css';

// $(function(es){
//     $(document).one('click', '.like-review', function(e) {
//         $(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
//         $(this).children('.fa-heart').addClass('animate-like');
//         $(es());
//     });
// });

$(function(){
	$(document).delegate('.like-review', 'click', function(e) {
		$(this).html('<i class="fa fa-heart" aria-hidden="true"></i> You liked this');
		$(this).children('.fa-heart').addClass('animate-like');
	});
});



     

class ListItem extends Component {
    kek(sd, q, w, e, r) {
        console.log(swal(sd));
        return swal({
            title: "Author: " + sd,
            text: "Origin: " + q + "\n" + "Portfolio url: " + w + "\n" + "Instagram username: @" + e + "\n" + "Location: " + r,
            icon: "info"
        });
    }
    render() {
        const { repo } = this.props;
        return (                    
            <div id="all-content">   
                <div class="container infinite-container" id="product_list">
                    <div class="infinite-item">
                        <div class="card border-success mb-3 text-center" id="card-a" >                            
                            <div class="card-body">
                                <img style={{width:'350px', height:'400px'}}src={repo.urls.regular} class="card-img-top"></img>                                
                                <h5 class="card-header" id="name">Author is {repo.user.name}</h5>                                                                                          
                                <div class="container"> 
                                <p></p>     
                                <button type="button" class="btn btn-danger" id="btn" onClick={()=>this.kek(
                                    `${repo.user.name}`,`${repo.links.html}`,`${repo.user.portfolio_url}`,
                                    `${repo.user.instagram_username}`, `${repo.user.location}`
                                    )}>Information</button>
                                <div class="like-content">  
                                    <button class="btn-secondary like-review" id="heart-btn">
                                    <i class="fa fa-heart" aria-hidden="true"></i>{repo.likes} Likes
                                    </button>  
                                </div>
                                </div>                             
                                <div><small id="s">Created at {repo.created_at}</small></div>                             
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default ListItem;
