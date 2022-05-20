import React from 'react'
import {useParams} from 'react-router-dom'
/*
всё работает, не трогать
*/
const ProjectItem = ({project}) => {
    return(
    <tr>
        <td>{project.name}</td>
        <td>{project.users}</td>
    </tr>
    )
}
const UserProList = ({projects}) => {
    var {id} = useParams()
    var filteredProjects = projects.filter((project) => project.users.includes(parseInt(id)))
    return(
    <table>
        <th>name</th>
        <th>users</th>
    {filteredProjects.map((project) => <ProjectItem project={project}/>)}
    </table>
    )
}

export default UserProList

/*
всё работает, не трогать
*/








