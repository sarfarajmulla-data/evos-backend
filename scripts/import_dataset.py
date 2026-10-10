from app.services.dataset_service import DatasetService

if __name__ == "__main__":
    service = DatasetService()
    result = service.import_dataset("fleet_summary", "mock/public/fleet_summary")
    print(result)
