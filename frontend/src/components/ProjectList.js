import {Link} from 'react-router-dom'
import React from 'react'

const ProjectItem = ({project, deleteProject}) => {
    return(
    <tr>
        <td><Link to={`/project/${project.id}`}> {project.name} </Link> </td>
        <td>{project.repository_url}</td>
        <td>{project.users}  </td>
        <td><button onClick={()=>deleteProject(project.id)}>Delete</button></td>
    </tr>
    )
}
const ProjectList = ({projects, deleteProject}) => {
    return(
    <table>
        <th>name</th>
        <th>repository_url</th>
        <th>users</th>
    {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}

    </table>
    )
}

export default ProjectList
