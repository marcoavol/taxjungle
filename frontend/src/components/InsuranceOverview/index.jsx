import React from 'react';
import {Link} from 'react-router-dom';
//img
/* import filter from '../../assets/icons/filter.svg'
import search from '../../assets/icons/search.svg'
import location from '../../assets/icons/location.svg' */

import purple_background6 from '../../assets/purple_background6.jpg';

import BlogHeaderComponent from '../../components/BlogOverview/BlogHeaderComponent';
import InsuranceCardComponent from '../InsuranceOverview/InsuranceCardComponent';
//css
import {BlogOverviewStyle} from '../BlogOverview/styles';

const InsuranceOverview =()=>{

    return(
        <BlogOverviewStyle>
            <h1 className="title">My Keen Blog</h1>
                <BlogHeaderComponent />
                
            <div className="main-container">
                <div className="card-box">
                    <InsuranceCardComponent />
                    <InsuranceCardComponent />
                    <InsuranceCardComponent />
                </div>
                <div className="back-img"></div>
            </div>
            
        </BlogOverviewStyle>
        
    )
}
export default InsuranceOverview;
