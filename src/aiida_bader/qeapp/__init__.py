from aiidalab_qe.common.panel import PluginOutline

from .resources import BaderResourceSettingsModel, BaderResourceSettingsPanel
from .workchain import workchain_and_builder
from .result import BaderResultsPanel, BaderResultsModel
from .setting import BaderConfigurationSettingPanel
from .model import BaderConfigurationSettingsModel
from .structure_examples import structure_examples
from pathlib import Path


class PluginOutline(PluginOutline):
    title = "Bader charge analysis"


bader = {
    "outline": PluginOutline,
    "structure_examples": structure_examples,
    "configuration": {
        "panel": BaderConfigurationSettingPanel,
        "model": BaderConfigurationSettingsModel,
    },
    "resources": {
        "panel": BaderResourceSettingsPanel,
        "model": BaderResourceSettingsModel,
    },
    "workchain": workchain_and_builder,
    "result": {
        "panel": BaderResultsPanel,
        "model": BaderResultsModel,
    },
    "guides": {
        "title": "Bader charge analysis",
        "path": Path(__file__).resolve().parent / "guides",
    },
    "metadata": {
        "process_labels": {
            "QeBaderWorkChain": "Bader charge workflow",
            "PpCalculation": "Compute charge density",
            "BaderCalculation": "Compute Bader charge",
        }
    },
}
