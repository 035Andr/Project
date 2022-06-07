import React from 'react'
import {useParams} from 'react-router-dom'


const TodoItem = ({todo, deleteTodo}) => {
    return(
    <tr>
        <td>{todo.is_active}</td>
        <td>{todo.project}</td>
        <td>{todo.user}</td>
        <td>{todo.title}</td>
        <td>{todo.text}</td>
        <td><button onClick={()=>deleteTodo(todo.id)}>Delete</button></td>

    </tr>
    )
}
const TodoList = ({todos, deleteTodo}) => {
    return(
    <table>
        <th> is_active </th>
        <th> project </th>
        <th> user </th>
        <th> title </th>
        <th> text </th>
    {todos.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo} />)}
    </table>
    )
}

export default TodoList


