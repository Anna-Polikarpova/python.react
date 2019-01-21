import React, { Component } from 'react'
import { Switch, Route, Link, withRouter } from 'react-router-dom';
import ReposList from './Repos/ReposList';
import './NAV.css';

export default class Navbar extends Component {
    render() {
        return(
            <nav className="navbar navbar-expand-sm navbar-dark px-sm-5" id="nv">                    
                <ul className="navbar-nav align-items-center">
                    <li className="nav-item ml-5">
                        <Link to="/list" className="nav-link">
                        <h3>Photos</h3>
                        </Link>
                    </li>
                </ul>
            </nav>
        );
    }
}