# Location: `sky/backends/cloud_vm_ray_backend.py`
...
def _get_cluster_config_template(cloud):
    ...
    cloud_to_template = {
        ...
        # TODO Add this
        clouds.FluffyCloud: 'fluffycloud-ray.yml.j2',
        ...
    }
    ...
...