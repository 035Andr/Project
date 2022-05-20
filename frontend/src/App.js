import React from 'react';
import axios from 'axios';
import Main from './components/Main.js';
import UserList from './components/UserList.js';
import ProjectList from './components/ProjectList.js';
import TodoList from './components/TodoList.js';

import UserProList from './components/UserProList.js';
import ProToList from './components/ProToList.js';

import LoginForm from './components/LoginForm.js'

import {BrowserRouter, Route, Routes, Link, useLocation, Navigate,} from 'react-router-dom'



const NotFound = () => {
    var location = useLocation()
    return (
        <div>
            Page "{location.pathname}" not found
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects' : [],
            'todos' : [],
            'token': ''
        }
    }

    obtainAuthToken(login, password) {
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {"username": login, "password": password})
            .then(response => {
                let token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState({
                    'users' : users
                })
            })
             .catch(error => {
                this.setState({
                    'users': []
                })
                console.log(error)
            })


        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState({
                    'projects' : projects
                })
            })
            .catch(error => {
                this.setState({
                    'project': []
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/todos/', {headers})
            .then(response => {
                const todos = response.data
                this.setState({
                    'todos' : todos
                })
            })
            .catch(error => {
                this.setState({
                    'todos': []
                })
                console.log(error)
            })
    }
    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/'><h3>Главная страница</h3></Link></li>
                            { this.isAuth() ? <button onClick={()=>this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                            <li><Link to='/users'><h4>Пользователи</h4></Link></li>
                            <li><Link to='/projects'><h4>Проекты</h4></Link></li>
                            <li><Link to='/todos'><h4>Заметки</h4></Link></li>
                        </ul>
                    </nav>
                    <Routes>
                        <Route exact path='/' element = {<Main/>} />
                         <Route exact path='/login' element = {<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />

                        <Route exact path='/users' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/projects' element = {<ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' element = {<TodoList todos={this.state.todos} />} />

                        <Route exact path='/user/:id' element = {<UserProList projects={this.state.projects} />} />
                        <Route exact path='/project/:id' element = {<ProToList todos={this.state.todos} />} />

                        <Route path= '*' element = {<NotFound/>} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App








