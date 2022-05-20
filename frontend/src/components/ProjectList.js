import {Link} from 'react-router-dom'
import React from 'react'

const ProjectItem = ({project}) => {
    return(
    <tr>
        <td><Link to={`/project/${project.id}`}> {project.name} </Link> </td>
        <td>{project.repository_url}</td>
        <td>{project.users}  </td>

    </tr>
    )
}
const ProjectList = ({projects}) => {
    return(
    <table>
        <th>name</th>
        <th>repository_url</th>
        <th>users</th>
    {projects.map((project) => <ProjectItem project={project}/>)}
    </table>
    )
}

export default ProjectList
