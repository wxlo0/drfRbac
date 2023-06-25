import http from "@/utils/http";

export async function roleUpdate(roleId, data) {
    return await http.put(`/user/role/update/${roleId}`, data)
}

export async function rolePermissionsList(roleId) {
    return await http.get(`/user/role/permissions/list/${roleId}`)
}
