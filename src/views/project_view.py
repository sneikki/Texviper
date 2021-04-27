from PySide2.QtCore import QObject, Slot

from views.view import View
from controllers.project_controller import project_controller

class ProjectView(View):
    def __init__(self, engine):
        super().__init__(engine)

        self.current_project = None

    @Slot(str)
    def open_project(self, project_id):
        project = project_controller.get_project_by_id(project_id)
        self.current_project = project
        open_view = self.root.findChild(QObject, 'projectView')
        open_view.setProperty('openProject', 'ddd')
        open_view.setProperty('openProjectName', project.name)

        self.load_project(project_id)

    def load_project(self, project_id):
        pass