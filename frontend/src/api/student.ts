import http from '@/utils/http'

export async function getStudentList() {
    return await http.get('/student/')
}

export async function getStudentOne() {
    return await http.get('/student/1/')
}

export async function createStudentOne() {
    return await http.post('/student/')
}

export async function updateStudentOne() {
    return await http.put('/student/1/')
}

export async function deleteStudentOne() {
    return await http.delete('/student/1/')
}
