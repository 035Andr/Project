import React from 'react'
import {useParams} from 'react-router-dom'


const TodoItem = ({todo}) => {
    return(
    <tr>
        <td>{todo.title}</td>
        <td>{todo.text}</td>
        <td>{todo.user}</td>
    </tr>
    )
}

const ProToList = ({todos}) => {
    var {project_id} = useParams()
    var filteredTodos = todos.filter((todo) => todo.projects.includes(parseInt(project_id)))

    return(
    <table>
        <th> is_active </th>
        <th> project </th>
        <th> user </th>
        <th> title </th>
        <th> text </th>
    {filteredTodos.map((todo) => <TodoItem todo={todo}/>)}
    </table>
    )
}
export default ProToList






