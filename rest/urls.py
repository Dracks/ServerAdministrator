from rest_framework import routers
from Deployment import views as deployment_views
from ServerAdministrator import views as admin_views

__author__ = 'dracks'


router = routers.DefaultRouter()
router.register('hosts', admin_views.HostViewSet)
router.register('ssh_user', admin_views.SshUserViewSet)
router.register('applications', deployment_views.ApplicationViewSet)
router.register('versions', deployment_views.VersionViewSet)
router.register('version_files', deployment_views.VersionFileViewSet)
router.register('config_files', deployment_views.ConfigFileViewSet)
router.register('config_file_params', deployment_views.ConfigFileParamViewSet)
router.register('deployment_applications', deployment_views.DeploymentApplicationViewSet)
router.register('demployment_application_params', deployment_views.DeploymentApplicationParamViewSet)

urlpatterns = router.urls