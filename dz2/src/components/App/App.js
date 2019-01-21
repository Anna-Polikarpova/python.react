import React, { Component } from 'react';
import { hot } from 'react-hot-loader';
import { connect } from 'react-redux';
import { Switch, Route, Link, withRouter } from 'react-router-dom';
import Navbar from './components/Navbar';
import About from './components/About';
import ReposList from './components/Repos/ReposList';

import './styles.css';
import Footer from './components/Footer';

export class App extends React.Component {    

    onRepoClick(repo) {
        this.setState({
            title: repo.name
        })
    }

    render() {
        return (
            <React.Fragment>
                <Navbar />
                <Switch>
                    <Route path="/list" component={ ReposList } />
                    <Route path="/details" component={ ReposList } />  
                    <Route path="/about" component={ About } />
                </Switch>
                <Footer />          
            </React.Fragment>
        )
    }
}

export default hot(module)(withRouter(App));