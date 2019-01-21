import React, { Component } from 'react'
import { Switch, Route, Link, withRouter } from 'react-router-dom';
import About from './About/About';

export default class Footer extends Component {
  render() {
    return (
        <footer class="footer-bottom-area">
        <div class="container">
          <span class="text-muted">
                <Link to="/about" className="link">
                    <small>О проекте</small>
                </Link>                        
          </span>
        </div>
        </footer>
    )
  }
}
