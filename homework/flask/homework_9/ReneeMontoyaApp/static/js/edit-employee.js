class EmployeeFormController {
    constructor() {
        this.email = ''
        this.name = ''
        this.departmentType = ''
        this.department = ''

        this.departmentTypeNode = null
        this.departmentIdNode = null

        this.init()
        this.addEventListeners()
    }

    init() {
        this.departmentTypeNode = document.getElementById('department_type')
        this.departmentIdNode = document.getElementById('department_id')
    }

    addEventListeners() {
        this.departmentTypeNode.addEventListener('change', (evt) => this.handleDepartmentTypeChange(evt))
    }

    handleDepartmentTypeChange({target}) {
        this.departmentType = target.value
        this.departmentIdNode.value = null
        this.departmentIdNode.dataset.type = this.departmentType
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new EmployeeFormController()
})
